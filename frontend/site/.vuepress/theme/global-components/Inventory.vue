<template>
  <div>
    <h1>Inventaire des données à ouvrir</h1>
    <table class="table">
      <thead>
        <tr>
          <th v-for="column in columns">{{ column }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="dataset in datasets">
          <td v-for="column in columns" v-html="getField(dataset, column)"></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Inventory',
  data () {
    return {
      datasets: [],
      columns: [
        "Titre du jeu de données",
        "Base de données ou applicatif",
        "Description du jeu de données",
        "Organisation",
        // "Producteurs (nombre de jeux de données)",
        "Statut d’ouverture",
        // "URL du jeu de données"
      ]
    }
  },
  methods: {
    getField (dataset, column) {
      const fields = dataset.fields
      if (column === "Titre du jeu de données" && fields["URL du jeu de données"]) {
        return `<a href="${fields['URL du jeu de données']}">${fields["Titre du jeu de données"]}</a>`
      } else {
        return fields[column]
      }
    }
  },
  mounted () {
    axios.get(`${this.$themeConfig.apiUrl}/inventaire`).then((res) => {
      this.datasets = res.data.records
    })
  }
}
</script>
