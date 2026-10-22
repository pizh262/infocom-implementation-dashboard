import { useEffect, useState } from "react";

const team = [
  { role: "Team Lead", name: "Тоторкулова Айхан" },
  { role: "Backend Developer", name: "Игнатова Анастасия" },
  { role: "Frontend Developer", name: "Тукаева Анастасия" },
];

export default function App() {
  const [backendStatus, setBackendStatus] = useState("Проверка...");

  useEffect(() => {
    fetch("/api/health")
      .then((response) => {
        if (!response.ok) throw new Error("Backend unavailable");
        return response.json();
      })
      .then((data) => setBackendStatus(data.status))
      .catch(() => setBackendStatus("недоступен"));
  }, []);

  return (
    <main style={{
      fontFamily: "Arial, sans-serif",
      maxWidth: 900,
      margin: "60px auto",
      padding: 24
    }}>
      <h1>Infocom Implementation Dashboard</h1>
      <p>Панель контроля внедрения информационных систем.</p>

      <h2>Состав команды</h2>
      <ul>
        {team.map((member) => (
          <li key={member.role}>
            <strong>{member.role}:</strong> {member.name}
          </li>
        ))}
      </ul>

      <h2>Состояние системы</h2>
      <p>Backend: {backendStatus}</p>
    </main>
  );
}
