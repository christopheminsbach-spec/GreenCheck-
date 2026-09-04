import {
    Link
} from "react-router-dom";


function Navbar(){


return (

<nav
className="
bg-white
shadow
px-8
py-4
flex
justify-between
items-center
"
>


<div>

<Link
to="/"
className="
text-2xl
font-bold
text-green-700
"
>

🌿 GreenCheck

</Link>


</div>




<div
className="
flex
gap-6
"
>


<Link
to="/dashboard"
className="
hover:text-green-600
"
>

Dashboard

</Link>


<Link
to="/diagnose"
className="
hover:text-green-600
"
>

Diagnostic

</Link>



<Link
to="/login"
className="
hover:text-green-600
"
>

Connexion

</Link>



</div>


</nav>

)


}


export default Navbar;