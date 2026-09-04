import GlassCard from "../components/ui/GlassCard";


export default function Result(){


return (

<div className="p-10">


<h1 className="text-4xl font-bold">

Diagnostic terminé

</h1>



<GlassCard className="mt-8">


<h2 className="text-2xl">

🍅 Tomate

</h2>



<div className="
text-red-500
text-xl
mt-4
">

Leaf Spot

</div>



<p className="mt-4">

Confiance :

<strong>

94%

</strong>

</p>


<hr className="my-6"/>



<h3>

Conseils

</h3>


<ul>

<li>
Supprimer les feuilles infectées
</li>

<li>
Améliorer la ventilation
</li>

<li>
Appliquer un traitement adapté
</li>


</ul>



</GlassCard>


</div>

)

}

