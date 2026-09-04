import {useState} from "react";
import api from "../api/axios";


export default function Diagnose(){


const [image,setImage]=useState(null);
const [result,setResult]=useState(null);



async function sendImage(){


const formData=new FormData();


formData.append(
    "image",
    image
);


const response =
await api.post(
    "/diagnose/",
    formData,
    {
        headers:{
            "Content-Type":"multipart/form-data"
        }
    }
);


setResult(response.data);


}



return (

<div>

<h1>
Diagnostic plante
</h1>


<input

type="file"

onChange={
(e)=>setImage(e.target.files[0])
}

/>


<button onClick={sendImage}>

Analyser

</button>


<pre>

{JSON.stringify(result,null,2)}

</pre>


</div>


)


}