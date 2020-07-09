<template>
  <div class="playlist-container">
    <PlaylistItem
      v-for="dataset in datasets"
      :dataset="dataset"
      :key="dataset"
    />
  </div>
</template>

<script>
import axios from 'axios'

async function getDatasets (playlist) {
  let datasets = []

  const [dataset, resource] = playlist.split('/')

  const url = `https://www.data.gouv.fr/api/1/datasets/${dataset}/resources/${resource}/`

  const resourceMeta = await axios.get(url)

  const content = await axios.get(resourceMeta.data.latest)

  datasets = content.data.split('\n')

  return datasets
}

export default {
  props: ['id'],
  data () {
    return {
      datasets: []
    }
  },
  async mounted () {
    const loader = this.$loading.show()
    const datasets = await getDatasets(this.id)
    this.datasets = datasets
    loader.hide()
  }
}
</script>

<style>
.playlist-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: start;
  align-items: auto;
  align-content: start
}

.playlist-item {
  flex: 0 0 auto;
  margin: 10px;
  width: 250px;
}
</style>
