function StatCard({icon, title, value}) {

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <div className="text-3xl">
                {icon}
            </div>


            <h3 className="text-gray-500 mt-3">
                {title}
            </h3>


            <p className="text-3xl font-bold text-green-700">
                {value}
            </p>

        </div>

    );

}


export default StatCard;