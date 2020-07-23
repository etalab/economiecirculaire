<template>
  <div>
    <div v-if="submited" class="notification success">
      Merci ! Votre demande a bien été envoyée.
    </div>
    <div v-if="error" class="notification error">
      Oups, quelque chose s'est mal passé 🤕. Vous pouvez réessayer ou nous contacter sur ouverture@data.gouv.fr.
    </div>
    <form v-if="!submited" @submit.prevent="submit">
      <h1>{{ title }}</h1>
      <div>
      Vous souhaitez réutiliser des données relatives à l'économie circulaire mais vous ne parvenez pas à trouver les données recherchées ? Vous pouvez nous adresser votre demande, en y apportant le plus d'informations possible. Nous ferons tout notre possible pour identifier le jeu de données et accélérer sa publication s'il n'est pas encore disponible en open data. 
      </div>
      <div class="form__group">
        <label class="required" for="description">Quelles données recherchez-vous ?</label>
        <textarea v-model="form.description" name="description" id="description" required></textarea>
      </div>
      <div class="form__group">
        <label for="title">S’il est connu, quel est le titre du jeu de données ou de la base recherché ?</label>
        <input v-model="form.title" type="text" value="" name="title" id="title">
      </div>
      <div class="form__group">
        <label for="organisation">Quelle est l’organisation susceptible de diffuser ce jeu de données ?</label>
        <input v-model="form.organisation" type="text" value="" name="organisation" id="organisation">
      </div>
      <div class="form__group">
        <label for="geo">Quelle granularité géographique recherchez-vous ?</label>
        <select v-model="form.geo" id="geo">
          <option></option>
          <option>Nationale</option>
          <option>Régionale</option>
          <option>Départementale</option>
          <option>EPCI</option>
          <option>Communale</option>
          <option>Adresse</option>
        </select>
      </div>
      <div class="form__group">
        <label for="update">Quelle fréquence de mise à jour serait la plus adaptée à votre usage du jeu de données ?</label>
        <select v-model="form.update" id="update">
          <option></option>
          <option>Annuelle</option>
          <option>Semestrielle</option>
          <option>Trimestrielle</option>
          <option>Mensuelle</option>
          <option>Hebdomadaire</option>
          <option>Quotidienne</option>
          <option>Temps réel</option>
        </select>
      </div>
      <div class="form__group">
        <label for="reuse">Quelle réutilisation de ces données envisagez-vous ?</label>
        <textarea v-model="form.reuse" name="reuse" id="reuse"></textarea>
      </div>
      <button class="button" type="submit" name="subscribe" id="submit">Valider</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    title: String
  },
  data () {
    return {
      form: {},
      submited: false,
      error: false
    }
  },
  methods: {
    submit () {
      const url = `${this.$themeConfig.apiUrl}/demande`
      axios.post(url, this.form).then(res => {
        this.submited = true
        this.error = false
      }).catch(err => {
        console.error(err)
        this.error = true
      })
    }
  }
}
</script>
