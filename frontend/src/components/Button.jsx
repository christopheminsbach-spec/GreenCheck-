export default function Button({
children
}){


return (

<button

className="
px-6
py-3
rounded-xl
font-semibold
text-white

bg-gradient-to-r

from-green-500

to-green-700

shadow-lg

hover:scale-105

transition

"

>

{children}

</button>

)

}