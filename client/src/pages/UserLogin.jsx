import { useState } from "react";
import { useNavigate } from "react-router-dom";

function UserLogin() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [login,setLogin] = useState(false)
  const navigate = useNavigate()
  async function LoginUser(username, password){
    const data = {
      "id": "4",
      "data": {
        "name": username,
        "password": password
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
    if (respjson["data"] === "Login Successful"){
        setLogin(true);
        return 1;
    }
    else{
        setLogin(false);
        return 0;
    }

  }
  return (
    <div className="p-[35vh]">
 
   <div className="flex items-center content-center justify-center pb-4">
    <h1 className="text-3xl font-sans font-bold justify-center text-white">👨‍🦱User Login</h1>
    </div>
      <div className="flex items-center content-center justify-center pt-6 pb-4">
      <div className="bg-slate-200 p-2 rounded-xl">
      <input className="bg-transparent placeholder:text-black focus:outline-none" placeholder="Name" onChange={(name)=>{setUsername(name.target.value)}}></input>
      </div>
     
      </div>
      <div className="flex items-center content-center justify-center pb-10 pt-1">
      <div className="bg-slate-200 p-2 rounded-xl">
      <input className="bg-transparent placeholder:text-black focus:outline-none" type="password" placeholder="Password" onChange={(pwd)=>{setPassword(pwd.target.value)}}></input>
      </div>

      </div>
      <div className="flex items-center content-center justify-center">
      <button type="button" className="bg-orange-500 text-white px-3 py-2 rounded-lg" onClick={async ()=>{const resp = await LoginUser(username, password); if(resp===1){navigate('/payment')}}}>Login</button>
      </div>
  
    
     
     
    </div>
  );
}

export default UserLogin;
