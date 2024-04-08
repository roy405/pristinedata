import React from 'react';
import { useLocation } from 'react-router-dom';
import NavBar from './NavBar';

function ProcessedDataDisplay() {
  const location = useLocation();
  const { data, columns, types } = location.state?.processedData || { data: [], columns: [], types: {} };

  // Function to convert boolean to string
  const displayValue = (value, type) => {
    if (type === 'Boolean') {
      return value ? "TRUE" : "FALSE";
    }
    return value;
  };

  return (
    <div className="container mx-auto p-4 bg-theme-light shadow rounded-lg">
      <h2 className="text-2xl font-bold text-theme mb-4">Processed Data</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white">
          <thead className="bg-theme text-white">
            <tr>
              {columns.map((column) => (
                <th key={column} className="text-left py-3 px-4 uppercase font-semibold text-sm">
                  {column} ({types[column] || 'Unknown'})
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="text-theme">
            {data.map((row, index) => (
              <tr key={index} className={index % 2 === 0 ? 'bg-white' : 'bg-blue-100'}>
                {columns.map((column) => (
                  <td key={column} className="text-left py-3 px-4">
                    {displayValue(row[column], types[column])}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default ProcessedDataDisplay;



