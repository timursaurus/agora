import { createStore } from 'vuex'
import HTTP from '@/api'
// import router from '@/router'

const store = createStore({
    state: {
        accessToken: null,
        refreshToken: null,
    },
    mutations: {
        setToken: (state, model) => {
            state.accessToken = model.access
            state.refreshToken = model.refresh
        },
        clearToken: (state) => {
            state.accessToken = null
            state.refreshToken = null
        }
    },
    getters: {
        isAuthenticated (state) {
            return state.accessToken != null && state.refreshToken != null
        }

    },
    actions: {
        SignIn: async ({ commit }, model) => {
            HTTP.post('api/token/', model)
            .then((res) => {
                commit('setToken', res.data)
            })
        },
        SignOut: ({ commit }) => {
            commit('clearToken')
        }
    }
})

export default store
