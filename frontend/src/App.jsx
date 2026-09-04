import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Diagnose from "./pages/Diagnose";

import MainLayout from "./layouts/MainLayout";

function App(){


return (

<Routes>


<Route
element={<MainLayout />}
>


<Route
path="/"
element={<Home />}
/>


<Route
path="/login"
element={<Login />}
/>


<Route
path="/register"
element={<Register />}
/>


<Route
path="/dashboard"
element={<Dashboard />}
/>


<Route
path="/diagnose"
element={<Diagnose />}
/>


</Route>


</Routes>

)

}


export default App;
