import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const apiUrl = `${process.env.REACT_APP_CODESPACE_NAME ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/` : 'http://localhost:8000/api/activities/'}`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Activities API endpoint:', apiUrl);
        console.log('Fetched activities:', data);
        setActivities(data.results || data);
      });
  }, [apiUrl]);

  return (
    <div className="card mt-4">
      <div className="card-body">
        <h2 className="card-title display-6 mb-4">Activities</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Tipo</th>
              <th>Duração (min)</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, idx) => (
              <tr key={idx}>
                <td>{activity.type}</td>
                <td>{activity.duration}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Activities;
