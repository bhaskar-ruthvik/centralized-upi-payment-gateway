import UserLogin from "./pages/UserLogin";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './index.css'
import MerchantLogin from "./pages/MerchantLogin";
import MerchantDashboard from "./pages/MerchantDashboard";
import UserRegistration from "./pages/UserRegistration";
import MerchantRegistration from "./pages/MerchantRegistration";
import Home from "./pages/Home";
import TransactionPage from "./pages/TransactionPage";
import Transactions from "./pages/Transactions";

function App() {
  return (
    <div className="App h-screen bg-slate-950" >
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/payment" element={<TransactionPage />}></Route>
        <Route path="/transactions" element={<Transactions />}></Route>
        <Route path="/userlogin" element={<UserLogin />}></Route>
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
