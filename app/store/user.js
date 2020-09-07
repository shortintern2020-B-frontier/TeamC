// Author: ZHANG CHI
export const state = () => ({
  userInfo: []
})

export const mutations = {
  add (state, object) {
      state.userInfo.push(object)
  }
}

export const actions = {
  getData (store) {
      setTimeout(() => {
          store.commit('add')
      }, 3000)
  }
}