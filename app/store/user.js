// Author: ZHANG CHI

const statusList = {
  0: { id: 0, title: "Free", class: "mdi mdi-emoticon-happy-outline" },
  1: { id: 1, title: "Busy", class: "mdi mdi-clock" },
  2: { id: 2, title: "Movie", class: "mdi mdi-movie-open" },
  3: { id: 3, title: "Karaoke", class: "mdi mdi-music-note-sixteenth" },
  4: { id: 4, title: "Food", class: "mdi mdi-pasta" },
  5: { id: 5, title: "Sports", class: "mdi mdi-basketball" },
  6: { id: 6, title: "Shopping", class: "mdi mdi-basket" },
  7: { id: 7, title: "Sleeping", class: "mdi mdi-power-sleep" },
}

export const state = () => ({
  userInfo: {},
  statusList: statusList
})

export const mutations = {
  add(state, object) {
    state.userInfo = object;
  }
}


export const actions = {
}