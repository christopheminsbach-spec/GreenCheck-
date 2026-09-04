import {
useState
} from "react";


import api from "../api/axios";


import DiagnosticCard
from "./DiagnosticCard";



export default function UploadPlant(){


const [image,setImage]=useState(null);

const [result,setResult]=useState(null);



const send=async()=>{


const form =
new FormData();


form.append(
"image",
image
);



const response =
await api.post(

"/diagnostics/upload/",

form

);



setResult(
response.data
);


};



return (

<div>


<input

type="file"

onChange={
e=>setImage(
e.target.files[0]
)
}

/>



<button

onClick={send}

>

Analyser

</button>



{

result &&

<DiagnosticCard

data={result}

/>

}


</div>


);


}