<template>
  <div id="json-form">
    <p>Version: {{ jsonForm.template_version }}</p>
    <div v-for="group in jsonForm.groups">
      <h1>{{ group.title }}</h1>
      <p>{{ group.description }}</p>
      <div v-for="question in group.questions" class="panel panel-primary">
        <div class="panel-heading">
          <h3 class="panel-title">{{ question.title }}</h3>
        </div>
        <div class="panel-body">
          <p>{{ question.comment }}</p>

          <input v-if="question.type==='input'" type="text" v-model="question.data" :placeholder="question.placeholder">
          <textarea v-if="question.type==='textarea'" v-model="question.data" :placeholder="question.placeholder"></textarea>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'app',
    data: function () {
      return {
        jsonForm: this.initialJsonForm
      }
    },
    props: {
      initialJsonForm: {
        type: Object,
        required: true
      }
    }
  }
</script>

<style>

</style>
