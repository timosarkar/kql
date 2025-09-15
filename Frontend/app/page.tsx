
"use client";

import { useState, useEffect } from "react";

export default function Home() {
  const [files, setFiles] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [search, setSearch] = useState("");
  const [content, setContent] = useState("");

  useEffect(() => {
    const kqlFiles = [
      "/Users/timo/projects/kql/XDR/MDVM/High Vulnerabilities.kql",
      "/Users/timo/projects/kql/XDR/MDVM/Critical Vulnerabilities.kql",
      "/Users/timo/projects/kql/XDR/Endpoints/Hunting for MacOS Devices.kql",
      "/Users/timo/projects/kql/XDR/Email/UrlClickEvents on Phishing Mails.kql",
      "/Users/timo/projects/kql/XDR/Email/Delivered Mails with SPF Failure.kql",
      "/Users/timo/projects/kql/XDR/Defender Advanced Hunting/Password Never Expires.kql",
      "/Users/timo/projects/kql/Sentinel/Potentially Suspicious MSHTA File.kql",
      "/Users/timo/projects/kql/Sentinel/HybridPetya Detection Rule.kql",
      "/Users/timo/projects/kql/Sentinel/Hunting for compromised npm packages.kql",
      "/Users/timo/projects/kql/Sentinel/Hunting for AutoRun Registry Modifications.kql",
      "/Users/timo/projects/kql/Sentinel/Hunt for vulnerable vibecoding editors.kql",
      "/Users/timo/projects/kql/Sentinel/Detect ClickFix Campaigns.kql",
    ];
    setFiles(kqlFiles);
  }, []);

  const filteredFiles = files.filter((file) =>
    file.toLowerCase().includes(search.toLowerCase())
  );

  const handleFileClick = async (file) => {
    setSelectedFile(file);
    try {
      const res = await fetch(`/api/file?path=${encodeURIComponent(file)}`);
      const data = await res.json();
      if (data.content) {
        setContent(data.content);
      } else {
        setContent("Error fetching file content.");
      }
    } catch (error) {
      setContent("Error fetching file content.");
    }
  };

  return (
    <div className="flex h-screen">
      <div className="w-1/4 bg-gray-100 p-4 overflow-y-auto">
        <input
          type="text"
          placeholder="Search KQL files..."
          className="w-full p-2 mb-4 border rounded"
          onChange={(e) => setSearch(e.target.value)}
        />
        <ul>
          {filteredFiles.map((file) => (
            <li
              key={file}
              className="cursor-pointer hover:bg-gray-200 p-2 rounded"
              onClick={() => handleFileClick(file)}
            >
              {file.split("/").pop()}
            </li>
          ))}
        </ul>
      </div>
      <div className="w-3/4 p-4">
        {selectedFile ? (
          <div>
            <h2 className="text-xl font-bold mb-4">
              {selectedFile.split("/").pop()}
            </h2>
            <pre className="bg-gray-200 p-4 rounded">
              {content}
            </pre>
          </div>
        ) : (
          <div className="flex items-center justify-center h-full">
            <p className="text-gray-500">Select a KQL file to view its content.</p>
          </div>
        )}
      </div>
    </div>
  );
}
