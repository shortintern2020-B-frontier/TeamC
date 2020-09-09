<!-- Author:Shun Kiyoura-->
<template>
  <v-layout column justify-center align-center>
    <v-container xs12 sm8 md6>
      <div class="text-center">
        <v-list three-line style="max-height: 500px" class="overflow-y-auto">
          <template v-for="room in rooms">
            <v-list-item true :key="room.chat_room_id" link :to="`/rooms/${room.id}`">
              <v-list-item-avatar>
                <v-img :src="avatar(room.users.find(n => n.id != id).id)"></v-img>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="room.users.find(n => n.id != id).username"></v-list-item-title>
                <v-list-item-subtitle v-html="room.last_chat.content"></v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </div>
    </v-container>
  </v-layout>
</template>

<script>
export default {
    async created() {
    const res = await this.$axios.get("/chat_rooms", {
      params: {
        id: this.$store.state.user.userInfo.id,
      },
    });
    this.rooms = res.data;
    console.log(this.rooms);
  },
  methods: {
    
  },

  data: () => ({
    rooms: [],
  }),
  computed: {
    avatar() {
      return (id) => {
        const imageLen = 10;
        console.log(id);
        return `/user_icon_${id % imageLen + 1}.jpg`;
      }
    },
  }
};
</script>
