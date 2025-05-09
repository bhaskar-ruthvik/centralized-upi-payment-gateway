import { useState } from "react";
import { useNavigate } from "react-router-dom";

function MerchantRegistration() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [ifsc,setIfsc] = useState("")
  const [amt,setAmt] = useState("")
  const navigate = useNavigate()
  async function RegisterUser(username, password, ifsc_code, amount_in_acc){
    const data = {
      "id": "1",
      "data": {
        "name": username,
        "password": password,
        "IFSC Code": ifsc_code,
        "Amount in Account": amount_in_acc,
      }
    }
    let fetchData = {
      method: 'POST',
      body: JSON.stringify(data),
      headers: new Headers({
  'Content-Type': 'application/json; charset=UTF-8'
})
    }
  

    const resp = await fetch('http://127.0.0.1:5000/bank_laptop',fetchData);
    const respjson = await resp.json();
    console.log(respjson)
    if (respjson["data"] === "Registration Complete"){
        return 1;
    }
    else{
        return 0;
    }

  }
  return (
    <div className="p-[25vh]">
 
   <div className="flex items-center content-center justify-center pb-4">
    <h1 className="text-3xl font-sans font-bold justify-center text-white">🧑‍💼Merchant Registration</h1>
    </div>
      <div className="flex items-center content-center justify-center pt-8 pb-4">
      <div className="bg-slate-200 p-2 rounded-xl">
      <input className="bg-transparent placeholder:text-black focus:outline-none" placeholder="Name" onChange={(name)=>{setUsername(name.target.value)}}></input>
      </div>
      </div>

      <div className="flex items-center content-center justify-center pt-1 pb-4">
      <div className="bg-slate-200 p-2 rounded-xl">
      <input className="bg-transparent placeholder:text-black focus:outline-none" placeholder="IFSC Code" onChange={(name)=>{setIfsc(name.target.value)}}></input>
      </div>
      </div>

      <div className="flex items-center content-center justify-center pt-1 pb-4">
      <div className="bg-slate-200 p-2 p rounded-xl">
      <input className="bg-transparent placeholder:text-black focus:outline-none" placeholder="Amount in Account" onChange={(name)=>{setAmt(name.target.value)}}></input>
      </div>
      </div>

      <div className="flex items-center content-center justify-center pb-10 pt-1">
      <div className="bg-slate-200 p-2 rounded-xl">
      <input className="bg-transparent placeholder:text-black focus:outline-none" type="password" placeholder="Password" onChange={(pwd)=>{setPassword(pwd.target.value)}}></input>
      </div>
      </div>

      <div className="flex items-center content-center justify-center">
      <button type="button" className="bg-orange-500 text-white px-3 py-2 rounded-lg" onClick={async ()=>{const resp = await RegisterUser(username, password,ifsc,amt); if(resp===1){navigate('/merchantdashboard')}}}>Register</button>
      </div>
  
    
     
     
    </div>
  );
}

export default MerchantRegistration;
