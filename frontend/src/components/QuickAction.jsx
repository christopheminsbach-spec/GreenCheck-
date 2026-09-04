function QuickAction({
    icon,
    title
}) {


return (

<div
className="
bg-green-50
rounded-2xl
p-6
cursor-pointer
hover:bg-green-100
transition
"
>


<div className="text-4xl">

{icon}

</div>


<h3
className="
font-bold
mt-4
text-lg
"
>

{title}

</h3>


</div>

)


}


export default QuickAction;