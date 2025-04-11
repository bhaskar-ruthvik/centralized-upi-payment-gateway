import { useEffect, useState } from "react";

export default function Transactions() {
    const [transactions, setTransactions] = useState([]);
    function convert_to_date(timestamp){
        const date = new Date(Math.round(1000*timestamp))
        return date.toDateString() + " " + date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
    }
    useEffect(() => {
        const fetchTransactions = async () => {
            const data = {
                "id": "7",
                "data": {}

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
                setTransactions(respjson["data"]["transactions"]);
                console.log(respjson["data"]["transactions"]);
            
        };

        fetchTransactions();
    }, [])
  return (
    <div className="h-screen bg-slate-950 py-[25vh] px-[8vw]">
       <div className="flex items-center content-center justify-center pb-4">
      <h1 className="text-3xl font-sans font-bold text-white">💰Transactions</h1>
      
    </div>
    <div className="flex overflow-auto">
    {transactions.length > 0 ? (
        <div className="flex">
            {transactions.map((transaction, index) => (
                
                <div key={index} className="bg-slate-700 p-4 rounded-xl m-4 text-white w-[20vw]">
                    <h1 className="font-bold py-4 w-[60%]">Current Hash: </h1>
                    <div className="bg-slate-200 py-2 px-3 rounded-xl overflow-auto">
                        <h1 className="font-bold text-black">{transaction["block_hash"]}</h1>
                    </div>
                    <h1 className="font-bold py-4 w-[60%]">Previous:</h1>
                    <div className="bg-slate-200 py-2 px-3 rounded-xl overflow-auto">
                        <h1 className="font-bold text-black">{transaction["previous_hash"]}</h1>
                    </div>
                    <h1 className="font-bold py-4 w-[60%]">Timestamp:</h1>
                    <div className="bg-slate-200 py-2 px-3 rounded-xl overflow-auto">
                    
                        <h1 className="font-bold text-black">{convert_to_date(transaction["timestamp"])}</h1>   
                    </div>
                </div>
            ))}
        </div>
      ) : <div className="flex"><h1 className="text-white">No Transactions</h1></div>
        }
    </div>
      
    </div>
 

  );
}