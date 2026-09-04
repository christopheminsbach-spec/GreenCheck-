import {useEffect,useState} from "react";

import api from "../services/api";


export default function Home(){

const [plants,setPlants]=useState([]);



useEffect(()=>{


api.get("/plants/")
.then(response=>{

setPlants(response.data)

})

.catch(error=>{

console.log(error)

})


},[]);



return (

<div>

<h1>
GreenCheck 🌱
</h1>


{
plants.map(
plant=>(

<div key={plant.id}>

<h3>
{plant.name}
</h3>

<p>
{plant.scientific_name}
</p>

</div>

)

)

}


</div>


)

}