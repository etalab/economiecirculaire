<template>
  <div style="margin-bottom: 1em;">
    <div v-html="html" />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['dataset'],
  data () {
    return {
      html: ''
    }
  },
  async mounted () {
    const url = `https://www.data.gouv.fr/api/1/oembed?url=${encodeURIComponent(this.dataset)}`
    const res = await axios.get(url)
    this.html = res.data.html
  }
}
</script>
