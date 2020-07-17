<template>
  <div>
    <h1>Inventaire des données à ouvrir</h1>
    <div v-if="!loading" style="margin-bottom: 10px;">
      <span class="badge green">{{ counters.open }} ouverts</span>
      <span class="badge orange">{{ counters.opening }} en cours d'ouverture</span>
      <span class="badge red">{{ counters.closed }} fermés</span>
      <span class="badge dark-grey">{{ counters.preview }} consultables uniquement</span>
    </div>
    <input v-model="query" type="text" class="table__filter" placeholder="Filtrer le tableau">
    <table class="table">
      <thead>
        <tr>
          <th v-for="column in columns">{{ column }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="dataset in filteredDatasets">
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
      query: '',
      datasets: [],
      columns: [
        "Titre du jeu de données",
        "Organisation",
        "Description du jeu de données",
        "Base de données ou applicatif",
        // "Producteurs (nombre de jeux de données)",
        "Statut d’ouverture",
        "Date estimée de publication",
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
          case 'Ouvert':
            _class = 'green'
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
    filteredDatasets () {
      if (this.query.length < 3) return this.datasets
      return this.datasets.filter(dataset => {
        return Object.keys(dataset.fields).some(field => {
          if (!dataset.fields[field] || !dataset.fields[field].toLowerCase) return false
          return dataset.fields[field].toLowerCase().includes(this.query)
        })
      })
    },
    counters () {
      const count = {
        'closed': 0,
        'opening': 0,
        'preview': 0,
        'open': 0
      }
      this.filteredDatasets.forEach(dataset => {
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
          case 'Ouvert':
            count.open += 1
            break
        }
      })
      return count
    }
  }
}
</script>

<style>
.table__filter {
  float: none;
}
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
  color: white;
}
.badge.dark-grey {
  background-color: #53657d;
  color: white;
}
</style>
