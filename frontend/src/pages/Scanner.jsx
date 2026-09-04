import {
Upload
}

from "lucide-react";


import GlassCard from "../components/ui/GlassCard";


export default function Scanner(){


return (

<div className="p-10">


<h1 className="text-4xl font-bold">

Scanner une plante

</h1>



<GlassCard className="
mt-10
text-center
">


<Upload

size={60}

className="
mx-auto
text-green-600
"

/>


<p className="mt-5">

Déposer une image de feuille

</p>



<button

className="
mt-6
bg-green-600
text-white
px-8
py-3
rounded-xl
"

>

Analyser avec IA

</button>


</GlassCard>


</div>

)

}
