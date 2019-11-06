<template>
    <Card>
        <h3>{{ dataset.title }}</h3>
        <div class="card__meta">
            <a v-if="dataset.organization" :href="dataset.organization.uri">{{ dataset.organization.name }}</a>
        </div>
        <p v-if="dataset.description">{{ dataset.description | truncate(240, '...') }}</p>
    </Card>
</template>

<script>
const axios = require('axios')

export default {
    props: ['slug'],
    data: ()=>{
        return {
            dataset: {
                resources: []
            },
            selected: false,
            clickable: false
        }
    },
    computed: {
        oembed(){
            // this.fetch()
            return "lol"
        }
    },
    async beforeMount(){
        const url = `https://www.data.gouv.fr/api/1/datasets/${this.slug}/`
        let response = await axios.get(url)

        this.$data.dataset = response.data

        console.log(this.$data.dataset)
    },
    methods: {
        _(txt){
            return txt
        },
        fetch(){
            console.log("yolo")

            // axios
            //     .get(`https://www.data.gouv.fr/api/1/datasets/${this.slug}/`)
            //     .then(response =>{
            //         this.dataset = response.data
            //     })
        }
    }
}
</script>
