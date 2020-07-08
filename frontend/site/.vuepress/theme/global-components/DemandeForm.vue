<template>
  <div>
    <div v-if="submited" class="notification success">
      Merci ! Votre demande a bien été envoyée.
    </div>
    <div v-if="error" class="notification error">
      Oups, quelque chose s'est mal passé 🤕. Vous pouvez réessayer ou nous contacter sur ouverture@data.gouv.fr.
    </div>
    <form v-if="!submited" @submit.prevent="submit">
      <div class="form__group">
        <label class="required" for="description">Quelles données recherchez-vous ?</label>
        <textarea v-model="form.description" name="description" id="description" required></textarea>
      </div>
      <div class="form__group">
        <label for="title">S’il est connu, quel est le titre du jeu de données recherché ?</label>
        <input v-model="form.title" type="text" value="" name="title" id="title">
      </div>
      <button class="button" type="submit" name="subscribe" id="submit">Valider</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
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
