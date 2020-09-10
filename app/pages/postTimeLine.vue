<!-- author Hiroki Okubo -->
<!-- Author Shotaro Murata -->
<template>
  <v-app style="margin:5%;">
    <v-main>
      <form align="center">
        <h1
          style="color: grey; display: inline-block; text-align: center; margin: 0 auto;"
        >
          Timeline
        </h1>
        <v-text-field
          color="deep-purple accent-3"
          v-model="place"
          :counter="30"
          label="Place"
          required
        ></v-text-field>
        <Datetime
          v-model="event_date"
          :minute-interval="10"
          :format="'YYYY-MM-DD HH:mm'"
          :overlay="true"
        ></Datetime>
        <v-text-field
          color="deep-purple accent-3"
          v-model="comment"
          :counter="10"
          label="Comment"
          required
        ></v-text-field>

        <v-btn class="mr-4" @click="submit">submit</v-btn>
        <v-btn @click="clear">clear</v-btn>
      </form>
    </v-main>
  </v-app>
</template>

<script>
// Author Shotaro Murata
import Datetime from "vue-ctk-date-time-picker";
import "@/node_modules/vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css";
export default {
  name: "timelinePost",
  components: { Datetime },
  data: () => ({
    place: "",
    event_date: "",
    comment: ""
  }),
  methods: {
    submit: async function() {
      const event_datetime = new Date(this.event_date).getTime();
      await this.$axios.$post("/timelines", {
        user_id: this.$store.state.user.userInfo.id,
        place: this.place,
        event_date: event_datetime,
        content: this.comment
      });
      this.$router.push("/timeline");
    },
    clear: function() {
      this.place = "";
      this.data = "";
      this.comment = "";
    }
  }
};
</script>
