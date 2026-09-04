import {
    useEffect,
    useState
} from "react";


import StatCard from "../components/StatCard";
import QuickAction from "../components/QuickAction";


function Dashboard(){


const [data,setData] = useState(null);



useEffect(()=>{


fetch(
"http://127.0.0.1:8000/api/dashboard/"
)

.then(
response => response.json()
)

.then(
result => setData(result)
)


},[]);



if(!data){

return (

<div className="
flex
justify-center
items-center
h-screen
">

Chargement GreenCheck 🌱

</div>

)

}



return (

<div
className="
p-8
space-y-10
"
>


{/* TITRE */}

<div>

<h1
className="
text-4xl
font-bold
text-green-700
"
>

🌿 Tableau de bord GreenCheck

</h1>


<p
className="
text-gray-500
mt-2
"
>

Analyse intelligente des plantes et reconnaissance IA

</p>


</div>





{/* STATISTIQUES */}


<div
className="
grid
md:grid-cols-3
gap-6
"
>


<StatCard

icon="🌱"

title="Plantes"

value={
data.plants_count
}

color="
text-green-600
"

/>



<StatCard

icon="👤"

title="Utilisateurs"

value={
data.users_count
}

color="
text-blue-600
"

/>



<StatCard

icon="📷"

title="Identifications"

value={
data.identifications_count
}

color="
text-purple-600
"

/>



</div>





{/* ACTIONS */}


<div>


<h2
className="
text-2xl
font-bold
mb-5
"
>

Actions rapides

</h2>



<div
className="
grid
md:grid-cols-3
gap-6
"
>


<QuickAction

icon="📷"

title="Identifier une plante"

/>


<QuickAction

icon="🌿"

title="Voir catalogue"

/>


<QuickAction

icon="🧠"

title="Analyse IA"

/>



</div>


</div>







{/* DERNIERES PLANTES */}


<div>


<h2
className="
text-2xl
font-bold
mb-5
"
>

Dernières plantes

</h2>


<div
className="
grid
md:grid-cols-3
gap-6
"
>


{
data.latest_plants?.map(
plant => (


<div
key={plant.id}
className="
bg-white
rounded-2xl
shadow
p-5
"
>


<div
className="
text-5xl
"
>
🌱
</div>


<h3
className="
font-bold
text-xl
mt-3
"
>

{plant.name}

</h3>


<p
className="
text-gray-500
"
>

{plant.scientific_name}

</p>


</div>


)

)

}



</div>


</div>





</div>

)


}


export default Dashboard;