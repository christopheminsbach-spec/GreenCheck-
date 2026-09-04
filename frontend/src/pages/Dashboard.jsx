import { useEffect, useState } from "react";

import api from "../services/api";

import StatCard from "../components/StatCard";
import PlantCard from "../components/PlantCard";


function Dashboard() {


    const [data, setData] = useState(null);



    useEffect(() => {

        api
        .get("/dashboard/")
        .then((response) => {

            setData(response.data);

        })
        .catch((error)=>{

            console.error(error);

        });


    }, []);



    if (!data) {

        return (
            <h2>
                Chargement Dashboard...
            </h2>
        );

    }



    return (

        <div className="p-8">


            <h1 className="text-3xl font-bold mb-8">

                🌿 GreenCheck Dashboard

            </h1>



            <div className="grid md:grid-cols-3 gap-6">


                <StatCard

                    icon="🌱"

                    title="Plantes"

                    value={data.plants_count}

                />


                <StatCard

                    icon="👤"

                    title="Utilisateurs"

                    value={data.users_count}

                />


                <StatCard

                    icon="📷"

                    title="Identifications"

                    value={data.identifications_count}

                />


            </div>



            <h2 className="text-2xl font-bold mt-10 mb-5">

                Dernières plantes

            </h2>



            <div className="grid md:grid-cols-3 gap-5">

                {data.latest_plants.map((plant)=>(

                    <PlantCard

                        key={plant.id}

                        plant={plant}

                    />

                ))}

            </div>


        </div>

    );

}


export default Dashboard;