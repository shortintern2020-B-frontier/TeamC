<template>
  <v-app>
    <v-main>
      <!-- <v-app-bar color="" dense></v-app-bar> -->
      <v-container class="fill-height" fluid>
        <v-container>
          <v-row dense>

            <v-card>タイムライン</v-card>
            <v-spacer></v-spacer>
            <v-col v-for="(timeline) in timelines_list" :key="timeline.id" cols="12">
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">{{
                      timeline.name
                    }}</span>
                  </v-avatar>
                  <div>
                    <v-card-title
                      class="headline"
                      v-text="timeline.statics"
                    ></v-card-title>
                    <v-card-subtitle>
                      {{ timeline.comment }} + {{ timeline.date }} + {{ timeline.place }}
                    </v-card-subtitle>
                  </div>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  layout: "home",
  data: () => ({
    // timelines_list: [
    //   {
    //     id: 0,
    //     name: "jonh",
    //     date: "2020/9/9",
    //     place: "Shinjyuku",
    //     comment: "だれか遊びに行きませんか？"
    //   },
    //   {
    //     id: 1,
    //     name: "jonh",
    //     date: "2020/9/9",
    //     place: "Shinjyuku",
    //     comment: "だれか遊びに行きませんか？"
    //   }
    // ],
    timelines_list: []
  }),
  methods: {
    findData: async function() {
      let userid = this.$store.state.user.userInfo.id;
      const res = await this.$axios.$get(
        "http://127.0.0.1:8000/timelines",
        {
          params: { id: userid }
        }
      );
      if (res != null) {
        this.timelines_list = res;
        console.log(this.timelines_list);
      }
    }
  },
  created() {
    this.findData();
  }
};
</script>
© 2020 GitHub, Inc.
