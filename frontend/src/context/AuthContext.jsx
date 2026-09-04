import {
createContext,
useState,
useContext
} from "react";


import api from "../api/axios";


const AuthContext =
createContext();



export function AuthProvider({children}){


const [user,setUser]=useState(null);



const login = async(data)=>{


const response =
await api.post(

"/login/",

data

);



localStorage.setItem(

"access",

response.data.access

);


localStorage.setItem(

"refresh",

response.data.refresh

);


setUser(data.username);


};



const logout=()=>{


localStorage.clear();

setUser(null);


};



return (

<AuthContext.Provider

value={{

user,
login,
logout

}}

>


{children}


</AuthContext.Provider>


);


}



export function useAuth(){

return useContext(AuthContext);

}
