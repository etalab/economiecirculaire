<template>
  <div>
    <h1>Inventaire des données à ouvrir</h1>
    <div v-if="!loading" style="margin-bottom: 10px;">
      <span class="badge orange">{{ counters.opening }} en cours d'ouverture</span>
      <span class="badge red">{{ counters.closed }} fermés</span>
      <span class="badge dark-grey">{{ counters.preview }} consultables uniquement</span>
    </div>
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
      loading: true,
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
      } else if (column === "Statut d’ouverture") {
        const value = fields['Statut d’ouverture']
        let _class = ''
        switch (value) {
          case 'Fermé':
            _class = 'red'
            break
          case 'Consultable uniquement':
            _class = 'dark-grey'
            break
          case 'En cours d’ouverture':
            _class = 'orange'
            break
        }
        return `<span class="badge ${_class}">${value}</span>`
      } else {
        return fields[column]
      }
    }
  },
  mounted () {
    const loader = this.$loading.show()
    axios.get(`${this.$themeConfig.apiUrl}/inventaire`).then((res) => {
      this.loading = false
      loader.hide()
      this.datasets = res.data.records
    })
  },
  computed: {
    counters () {
      const count = {
        'closed': 0,
        'opening': 0,
        'preview': 0
      }
      this.datasets.forEach(dataset => {
        switch (dataset.fields['Statut d’ouverture']) {
          case 'Fermé':
            count.closed += 1
            break
          case 'Consultable uniquement':
            count.preview += 1
            break
          case 'En cours d’ouverture':
            count.opening += 1
            break
        }
      })
      return count
    }
  }
}
</script>

<style>
.badge {
  border-radius: 4px;
  padding: 4px;
  font-size: 0.9em;
}
.badge.orange {
  background-color: #ff9947;
}
.badge.red {
  background-color: #d63626;
  color: white;
}
.badge.green {
  background-color: #03bd5b;
}
.badge.dark-grey {
  background-color: #53657d;
  color: white;
}
</style>
