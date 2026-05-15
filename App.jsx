
import { useState } from "react";
import axios from "axios";

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateImage = async () => {
    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/generate",
        { prompt }
      );

      setImage("http://127.0.0.1:8000/" + res.data.image_path);
    } catch (err) {
      alert("Error generating image");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🎨 Artify</h1>
      <p>AI Text-to-Image Generator</p>

      <textarea
        placeholder="Describe your imagination..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button onClick={generateImage}>
        {loading ? "Generating..." : "Generate Image"}
      </button>

      {image && (
        <div className="image-box">
          <img src={image} alt="Generated" />
        </div>
      )}
    </div>
  );
}
