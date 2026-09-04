function PlantCard({plant}) {

    return (

        <div className="bg-white rounded-xl shadow p-4">

            <h3 className="font-bold text-lg">
                🌱 {plant.name}
            </h3>


            <p className="italic text-gray-500">
                {plant.scientific_name}
            </p>

        </div>

    );

}


export default PlantCard;