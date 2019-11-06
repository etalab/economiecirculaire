<template>
    <div>
        <PlaylistItem
            v-for="dataset in datasets"
            :dataset="dataset"
        />
    </div>
</template>

<script>
import axios from 'axios'

async function get_datasets(playlist){
    let datasets = []

    const [dataset, resource] = playlist.split("/")

    const url = `https://www.data.gouv.fr/api/1/datasets/${dataset}/resources/${resource}/`

    const resource_meta = await axios.get(url)

    const content = await axios.get(resource_meta.data.latest)

    datasets = content.data.split("\n")

    return datasets
}

export default {
    props: ["id"],
    data () {
        return {
            datasets: []
        }
    },
    async mounted () {
        const datasets = await get_datasets(this.id)
        this.datasets = datasets
        console.log(datasets)
    }
}
</script>
