import UserLogin from "./pages/UserLogin";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './index.css'
import UserDashboard from "./pages/UserDashboard";
import MerchantLogin from "./pages/MerchantLogin";
import MerchantDashboard from "./pages/MerchantDashboard";
import UserRegistration from "./pages/UserRegistration";
import MerchantRegistration from "./pages/MerchantRegistration";

function App() {
  return (
    <div className="App h-screen bg-slate-950" >
    <BrowserRouter>
      <Routes>
        <Route path="/userlogin" element={<UserLogin />}></Route>
        <Route path="/userdashboard" element={<UserDashboard />}></Route>
        <Route path="/userregister" element={<UserRegistration/>}></Route>
        <Route path="/merchantlogin" element={<MerchantLogin />}></Route>
        <Route path="/merchantdashboard" element={<MerchantDashboard />}></Route>
        <Route path="/merchantregister" element={<MerchantRegistration /> }></Route>
      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
