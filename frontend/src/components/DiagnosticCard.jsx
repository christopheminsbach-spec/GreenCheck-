export default function DiagnosticCard({
data
}){


return (

<div
className="border p-5 rounded"
>


<h2>

Diagnostic

</h2>


<p>

🌿 Résultat :
{data.prediction}

</p>


<p>

Confiance :
{data.confidence*100} %

</p>


<p>

Conseil :

{data.advice}

</p>


<a

href={
`http://localhost:8000/media/${data.image}`
}

>

Voir image

</a>


</div>

);


}