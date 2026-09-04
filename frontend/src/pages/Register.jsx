import {
useState
} from "react";


import api from "../api/axios";


import {
useNavigate
} from "react-router-dom";



export default function Register(){


const navigate =
useNavigate();


const [form,setForm]=useState({});


const submit=async(e)=>{


e.preventDefault();


await api.post(

"/register/",

form

);


navigate("/login");


};



return (

<form onSubmit={submit}
className="p-10">


<h1>
Créer un compte
</h1>


<input

placeholder="Username"

onChange={
e=>setForm({
...form,
username:e.target.value
})
}

/>



<input

placeholder="Email"

onChange={
e=>setForm({
...form,
email:e.target.value
})
}

/>



<input

type="password"

placeholder="Password"

onChange={
e=>setForm({
...form,
password:e.target.value
})
}

/>



<button>

Créer

</button>


</form>

);


}