function StatCard({
    icon,
    title,
    value,
    color
}) {


    return (

        <div
            className="
            bg-white
            rounded-3xl
            shadow-lg
            p-6
            hover:-translate-y-1
            transition
            "
        >

            <div
                className={`
                text-4xl
                ${color}
                `}
            >
                {icon}
            </div>


            <p
                className="
                text-gray-500
                mt-4
                "
            >
                {title}
            </p>


            <h2
                className="
                text-4xl
                font-bold
                mt-2
                "
            >
                {value}
            </h2>


        </div>

    )

}


export default StatCard;