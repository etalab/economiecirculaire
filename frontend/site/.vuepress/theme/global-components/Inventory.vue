<template>
  <div>
    <h1>Inventaire des données à ouvrir</h1>
    <div v-if="!loading" style="margin-bottom: 10px;">
      <span v-for="s in statuses" @click="toggle(s.key)" class="badge" :class="[!s.visible ? 'disabled' : '', s._class]">
        {{ counters[s.key] }} {{ s.labelExtended }}
      </span>
    </div>
    <input v-model="query" type="text" class="table__filter" placeholder="Filtrer le tableau" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
    <table class="table">
      <thead>
        <tr>
          <th v-for="column in columns">{{ column }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="dataset in filteredDatasetsByStatus">
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
      statuses: [
        {label: "Ouvert", key: "open", visible: true, _class: "green", labelExtended: "ouverts"},
        {label: "En cours d’ouverture", key: "opening", visible: true, _class: "orange", labelExtended: "en cours d’ouverture"},
        {label: "Consultable uniquement", key: "preview", visible: true, _class: "dark-grey", labelExtended: "consultables uniquement"},
        {label: "Fermé", key: "closed", visible: true, _class: "red", labelExtended: "fermés"},
      ],
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
    toggle (badge) {
      const status = this.statuses.find(s => s.key == badge)
      status.visible = !status.visible
    },
    getField (dataset, column) {
      const fields = dataset.fields
      if (column === "Titre du jeu de données" && fields["URL du jeu de données"]) {
        return `<a href="${fields['URL du jeu de données']}">${fields["Titre du jeu de données"]}</a>`
      } else if (column === "Statut d’ouverture") {
        const value = fields['Statut d’ouverture']
        const status = this.statuses.find(s => s.label == value)
        if (!status) {
          return value
        }
        return `<span class="badge ${status._class}">${value}</span>`
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
    filteredDatasetsByStatus () {
      const visibleStatuses = this.statuses.filter(s => s.visible).map(s => s.label)
      return this.filteredDatasets.filter(dataset => {
        return visibleStatuses.indexOf(dataset.fields["Statut d’ouverture"]) >= 0
      })
    },
    filteredDatasets () {
      if (this.query.length < 3) return this.datasets
      return this.datasets.filter(dataset => {
        return Object.keys(dataset.fields).some(field => {
          if (!dataset.fields[field] || !dataset.fields[field].toLowerCase) return false
          return dataset.fields[field].toLowerCase().includes(this.query.toLowerCase())
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
        const value = dataset.fields['Statut d’ouverture']
        const status = this.statuses.find(s => s.label == value)
        if (status) {
          count[status.key] += 1
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
  cursor: pointer;
  margin-right: 5px;
}
.badge.disabled {
  opacity: 0.5;
  /* color: black !important; */
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
