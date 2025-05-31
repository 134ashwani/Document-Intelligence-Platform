import { useState } from 'react';

export default function Home() {
  const [file, setFile] = useState(null);
  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch('http://127.0.0.1:8000/api/upload/', {
      method: 'POST',
      body: formData,
    });
    const data = await res.json();
    console.log(data);
  };
  return (
    <div>
      <h1>Upload Document</h1>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}
