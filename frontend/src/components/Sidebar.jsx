import {

Leaf,

Scan,

LayoutDashboard

}

from "lucide-react";


export default function Sidebar(){


return (

<aside

className="
w-72
min-h-screen
bg-white
p-6
shadow-xl

"


>


<h1 className="
text-2xl
font-bold
text-green-600
">

🌱 GreenCheck

</h1>


<nav className="mt-10 space-y-5">


<div>
<LayoutDashboard/>
Dashboard
</div>


<div>
<Scan/>
Scanner IA
</div>


<div>
<Leaf/>
Plantes
</div>


</nav>


</aside>


)

}
