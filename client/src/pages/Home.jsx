import { useNavigate } from "react-router-dom";
export default function Home(){
    const navigate = useNavigate()
    return (
        <div>
              <div className="p-[35vh]">
 
 <div className="flex items-center content-center justify-center pb-4">
  <h1 className="text-3xl font-sans font-bold justify-center text-white">🪙UPI Payment Gateway</h1>
  </div>
    <div className="flex items-center content-center justify-center pt-6 pb-4">
    <div className="bg-slate-200 p-2 rounded-xl" onClick={()=>{navigate('/userregister')}}>
    <h1 className="font-bold">User Register</h1>
    </div>
   
    </div>
    <div className="flex items-center content-center justify-center pt-2 pb-4">
    <div className="bg-slate-200 p-2 rounded-xl" onClick={()=>{navigate('/transactions')}}>
   <h1 className="font-bold">See Transactions - Blockchain</h1>
    </div>
    </div>
    <div className="flex items-center content-center justify-center pt-2 pb-4">
    <div className="bg-slate-200 p-2 rounded-xl" onClick={()=>{navigate('/merchantregister')}}>
   <h1 className="font-bold">Merchant Register</h1>
    </div>

    </div>
    <div className="flex items-center content-center justify-center pt-2 pb-4">
    <div className="bg-slate-200 p-2 rounded-xl" onClick={()=>{navigate('/payment')}}>
   <h1 className="font-bold">Make a Payment</h1>
    </div>
    </div>
    <div className="flex items-center content-center justify-center pt-2">
    <div className="bg-slate-200 p-2 rounded-xl" onClick={()=>{navigate('/merchantdashboard')}}>
   <h1 className="font-bold">Generate QR Code</h1>
    </div>
    
    </div>
  
   
   
  </div>
        </div>
    )
}