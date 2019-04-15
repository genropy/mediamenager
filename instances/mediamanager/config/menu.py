# encoding: utf-8
def config(root,application=None):
    med = root.branch(u"!!Gestione media")
    med.branch('!!Documenti',pkg='docu')
    med.branch('!!Task',pkg='erpy_task')
    conf = med.branch('!!Configurazioni',tags='_DEV_')
    conf.branch('!!Anagrafiche',pkg='erpy_base')
    conf.branch('!!Contabilita',pkg='erpy_coge')
    conf.branch('!!Admin',pkg='adm')
