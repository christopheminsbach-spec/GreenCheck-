export default function GlassCard({
children,
className=""
}){


return (

<div

className={`
bg-white/70
backdrop-blur-xl
rounded-4xl
shadow-glass
border
border-white/50
p-6
${className}
`}

>

{children}

</div>

)

}