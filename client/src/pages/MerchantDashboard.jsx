import { useState } from "react";

function MerchantDashboard() {
  const [input, setInput] = useState("");
  const [qrValue, setQrValue] = useState(false);
  const [fileName, setFileName] = useState("");
  const generateQRCode = async () => {

    const data = {
        "id": "6",
        "data": {
          "MID": input
        }
      }
      let fetchData = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: new Headers({
    'Content-Type': 'application/json; charset=UTF-8'
  })
      }
    
  
      const resp = await fetch('http://127.0.0.1:5000/upi',fetchData);
      const respjson = await resp.json();
      console.log(respjson)
      if (respjson["data"]["status"] === "QR Generated Successfully"){
        console.log("QR Generated Successfully");
        setQrValue(true);
        setFileName(respjson["data"]["file_name"]);
          return 1;
      }
      else{
          return 0;
      }
  };

  return (
    <div className="p-[10vh]">
      <h1 className="text-3xl text-white font-bold mb-6 text-center">
      🔑Generate QR Code
      </h1>

      <div className="flex justify-center pt-4 pb-6 mb-4">
        <input
          className="bg-slate-200 p-2 rounded-lg text-black focus:outline-none placeholder:text-black"
          type="text"
          placeholder="Enter MID"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
      </div>

      <div className="flex justify-center mb-6">
        <button
        type="button"
          className="bg-orange-400 text-white px-4 py-2 rounded-lg"
          onClick={() => {generateQRCode()}}
        >
          Generate QR Code
        </button>
      </div>

      {qrValue && (
        <div className="flex justify-center">
         <img src={`qrs/${input}/${fileName}.png`} alt="qr-code"></img>
        </div>
      )}
    </div>
  );
}

export default MerchantDashboard;