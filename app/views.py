from django.contrib.auth.models import User
from django.db.models import Q, QuerySet
from django.shortcuts import render, redirect
from django.views.generic import View, ListView

from users.models import Profile
from .models import Categoria, Projeto, UsuarioAceito, UsuarioRecusado, UsuarioBanido, UsuarioAdvertido, \
    UsuarioGratificado, UsuarioConvidado


class MeusProjetosView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        q = Projeto.projetos_que_participa(request.user)

        return render(request, 'dashboard/meus_projetos.html',
                      {'current': 'projetos',
                       'andamento': q.filter(encerrado=False)[:5],
                       'encerrado': q.filter(encerrado=True)[:5],
                       'success': request.session.pop('success', None),
                       'error': request.session.pop('error', None),
                       'warning': request.session.pop('warning', None),
                       'qtd_notifications': ver_qtd_notificacoes(request.user)})


class ProjetoDetailView(View):
    @staticmethod
    def get(request, url_hash, *args, **kwargs):
        try:
            p = Projeto.objects.get(url_hash=url_hash)
            advertidos = [item.user.id for item in UsuarioAdvertido.objects.filter(projeto=p)]
            gratificados = [item.user.id for item in UsuarioGratificado.objects.filter(projeto=p)]
            aceitos = [item.user for item in UsuarioAceito.objects.filter(projeto=p)]

            if request.user in aceitos:
                return render(request, 'dashboard/projetos/detail_projeto.html',
                              {'project': p,
                               'participantes': aceitos,
                               'moderator': p.moderador,
                               'administrador': p.administrador,
                               'criador': p.criador,
                               'success': request.session.pop('success', None),
                               'error': request.session.pop('error', None),
                               'warning': request.session.pop('warning', None),
                               'advertidos': advertidos,
                               'gratificados': gratificados,
                               'qtd_notifications': ver_qtd_notificacoes(request.user)
                               })
            else:
                if len(UsuarioRecusado.objects.filter(projeto=p, user=request.user)) > 0:
                    return render(request, 'dashboard/projetos/detail_projeto.html',
                                  {'not_exists': True,
                                   'error': 'Infelizmente você foi recusado deste projeto :(',
                                   'qtd_notifications': ver_qtd_notificacoes(request.user)})

                if len(UsuarioBanido.objects.filter(projeto=p, user=request.user)) > 0:
                    return render(request, 'dashboard/projetos/detail_projeto.html',
                                  {'not_exists': True,
                                   'error': 'Você foi banido deste projeto. Isso irá impactar na sua reputação :(',
                                   'qtd_notifications': ver_qtd_notificacoes(request.user)})

                if p.encerrado:
                    return render(request, 'dashboard/projetos/detail_projeto.html',
                                  {'not_exists': True,
                                   'error': 'Este projeto já foi encerrado',
                                   'qtd_notifications': ver_qtd_notificacoes(request.user)})

                if p.privado:
                    return render(request, 'dashboard/projetos/detail_projeto.html',
                                  {'not_exists': True,
                                   'error': 'Você não pode ver esse projeto',
                                   'qtd_notifications': ver_qtd_notificacoes(request.user)})

                return render(request, 'dashboard/projetos/detail_projeto.html',
                              {'project': p,
                               'visitant': True,
                               'solicitar': True if len(p.pendentes.all().filter(id=request.user.id)) == 0 else False,
                               'success': request.session.pop('success', None),
                               'error': request.session.pop('error', None),
                               'warning': request.session.pop('warning', None),
                               'qtd_notifications': ver_qtd_notificacoes(request.user)
                               })
        except Projeto.DoesNotExist:
            return render(request, 'dashboard/projetos/detail_projeto.html',
                          {'not_exists': True,
                           'error': 'Este projeto não existe',
                           'qtd_notifications': ver_qtd_notificacoes(request.user)})


class ProjetosAndamentoView(ListView):
    template_name = 'dashboard/projetos/explore.html'
    paginate_by = 8
    context_object_name = 'all_projetos'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ProjetosAndamentoView, self).get_context_data(object_list=object_list, **kwargs)
        data['current'] = 'projetos-andamento'
        data['success'] = self.request.session.pop('success', None)
        data['error'] = self.request.session.pop('error', None)
        data['warning'] = self.request.session.pop('success', None)
        data['name'] = 'Projetos em andamento'
        data['empty'] = 'Nenhum projeto em andamento :('
        data['qtd_notifications'] = ver_qtd_notificacoes(self.request.user)

        return data

    def get_queryset(self):
        return Projeto.projetos_que_participa(self.request.user).filter(encerrado=False)


class ProjetosEncerradoView(ListView):
    template_name = 'dashboard/projetos/explore.html'
    paginate_by = 8
    context_object_name = 'all_projetos'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ProjetosEncerradoView, self).get_context_data(object_list=object_list, **kwargs)
        data['current'] = 'projetos-encerrado'
        data['success'] = self.request.session.pop('success', None)
        data['error'] = self.request.session.pop('error', None)
        data['warning'] = self.request.session.pop('success', None)
        data['name'] = 'Projetos encerrados'
        data['empty'] = 'Nenhum projeto encerrado :('
        data['qtd_notifications'] = ver_qtd_notificacoes(self.request.user)

        return data

    def get_queryset(self):
        return Projeto.projetos_que_participa(self.request.user).filter(encerrado=True)


class ConquistaView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'dashboard/meus_projetos.html',
                      {'current': 'conquistas',
                       'qtd_notifications': ver_qtd_notificacoes(request.user)})


class ExploreView(ListView):
    template_name = 'dashboard/projetos/explore.html'
    paginate_by = 8
    context_object_name = 'all_projetos'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ExploreView, self).get_context_data(object_list=object_list, **kwargs)
        data['current'] = 'explore'
        data['success'] = self.request.session.pop('success', None)
        data['error'] = self.request.session.pop('error', None)
        data['warning'] = self.request.session.pop('success', None)
        data['empty'] = 'Nenhum projeto foi encontrado :('
        data['name'] = 'Explorar Projetos'
        data['qtd_notifications'] = ver_qtd_notificacoes(self.request.user)

        return data

    def get_queryset(self):
        return Projeto.projetos_para_explorar(self.request.user).order_by('-data_criacao')


class SuggestionsView(ListView):
    template_name = 'dashboard/projetos/explore.html'
    context_object_name = 'all_projetos'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(SuggestionsView, self).get_context_data(object_list=object_list, **kwargs)
        data['current'] = 'suggestions'
        data['success'] = self.request.session.pop('success', None)
        data['error'] = self.request.session.pop('error', None)
        data['warning'] = self.request.session.pop('success', None)
        data['empty'] = 'Você não possui nenhum interesse, para resolver isso vá na aba perfil e adicione alguns!' if \
            self.get_queryset() is None else 'Desculpe, não foi encontrada nenhuma sugestão baseada nos seus ' \
                                             'interesses :( '
        data['name'] = 'Sugestões'
        data['qtd_notifications'] = ver_qtd_notificacoes(self.request.user)

        return data

    def get_queryset(self):
        interesses: QuerySet[Categoria] = self.request.user.profile.interesses.all()

        if len(interesses) == 0:
            return None
        return Projeto.projetos_para_explorar(self.request.user).filter(Q(categoria__in=interesses)).order_by('?')[:3]


class PesquisadoresView(ListView):
    template_name = 'dashboard/user/explore.html'
    context_object_name = 'all_users'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(PesquisadoresView, self).get_context_data(object_list=object_list, **kwargs)
        data['current'] = 'users'
        data['success'] = self.request.session.pop('success', None)
        data['error'] = self.request.session.pop('error', None)
        data['warning'] = self.request.session.pop('warning', None)
        data['empty'] = 'Nenhum pesquisador encontrado :('
        data['name'] = 'Explorar Pesquisadores'
        data['categorias'] = Categoria.objects.filter().order_by('nome')
        data['projetos'] = Projeto.projetos_com_acesso(self.request.user) if len(Projeto.projetos_com_acesso(self.request.user)) > 0 else False
        data['qtd_notifications'] = ver_qtd_notificacoes(self.request.user)

        return data

    def get_queryset(self, *args, **kwargs):
        cat = Categoria.objects.filter(id__in=[int(x) for x in self.request.GET.getlist('categorias')])

        if len(cat) > 0:
            return User.objects.filter(profile__mostrar_perfil=True, is_active=True, is_superuser=False, id__in=[x.get('user') for x in Profile.objects.filter(Q(interesses__in=cat)).values('user')]).exclude(id=self.request.user.id).\
                order_by('-profile__perfil_classifier')
        else:
            return User.objects.filter(profile__mostrar_perfil=True, is_active=True, is_superuser=False).exclude(
                id=self.request.user.id). \
                order_by('-profile__perfil_classifier')


class CriarProjetoView(View):
    @staticmethod
    def get(request, *args, **kwargs):

        return render(request, 'dashboard/projetos/criar_projeto.html', {'categorias': Categoria.objects.all(),
                                                                         'error': request.session.pop('error', None),
                                                                         'nome': request.session.pop('nome', None),
                                                                         'descricao': request.session.pop('descricao',
                                                                                                          None),
                                                                         'privado': request.session.pop('privado',
                                                                                                        None), })

    @staticmethod
    def post(request, *args, **kwargs):
        categorias = request.POST.getlist('categorias')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        privado = True if request.POST.get('privado') is not None else False

        list_categorias = add_categorias(categorias)

        if len(list_categorias) < 1:
            request.session['error'] = 'Adicione ao menos uma categoria'
            request.session['nome'] = nome
            request.session['descricao'] = descricao
            request.session['privado'] = privado

            return redirect('criar-projeto')
        else:
            p = Projeto(nome=nome,
                        descricao=descricao,
                        privado=privado,
                        criador=request.user)
            p.save()
            [p.categoria.add(kek.id) for kek in list_categorias]
            UsuarioAceito.salvar(p, request.user, True)

            return redirect('projetos')


class EncerrarProjetoView(View):
    @staticmethod
    def post(request, share_hash, secret_hash, *args, **kwargs):
        try:
            projeto: Projeto = Projeto.objects.get(share_hash=share_hash)
            user: User = User.objects.get(profile__secret_hash=secret_hash)

            if projeto.criador == user:
                projeto.encerrado = True
                projeto.save()
                request.session['error'] = 'Este projeto foi encerrado'
                return redirect('projeto-detail', url_hash=projeto.url_hash)
            else:
                request.session['error'] = 'Você não tem autorização, e não deveria ter feito isso >:('
                return redirect('projeto-detail', url_hash=projeto.url_hash)

        except Projeto.DoesNotExist:
            request.session['error'] = 'Como que você realizou este POST?'
            return redirect('projetos')


class MeuPerfilView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'dashboard/user/profile.html',
                      {'current': 'profile',
                       'categorias': Categoria.objects.all(),
                       'success': request.session.pop('success', None),
                       'error': request.session.pop('error', None),
                       'warning': request.session.pop('warning', None),
                       'qtd_notifications': ver_qtd_notificacoes(request.user)
                       })

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            desc = request.POST.get('descricao')
            interesses = request.POST.getlist('interesses')
            privado = False if request.POST.get('privado', True) == 'privado' else True

            profile: Profile = Profile.objects.get(user=request.user)

            profile.descricao = desc
            profile.mostrar_perfil = privado
            profile.interesses.clear()
            [profile.interesses.add(item.id) for item in add_categorias(interesses)]
            profile.save()

            request.session['success'] = 'Perfil alterado com sucesso'
            return redirect('meu-perfil')
        except Profile.DoesNotExist:
            request.session['error'] = 'Não faça esse tipo de coisa >:( É errado e você sabe!'
            return redirect('meu-perfil')


class PerfilView(View):
    @staticmethod
    def get(request, profile_hash, *args, **kwargs):
        try:
            p = Profile.objects.get(url_hash=profile_hash)

            if request.user.id == p.user.id:
                return redirect('meu-perfil')

            return render(request, 'dashboard/user/profile_detail.html',
                          {'profile': p,
                           'projetos': Projeto.projetos_com_acesso(request.user),
                           'qtd_notifications': ver_qtd_notificacoes(request.user)})
        except Profile.DoesNotExist:
            return render(request, 'dashboard/user/profile_detail.html',
                          {'not_exists': True,
                           'qtd_notifications': ver_qtd_notificacoes(request.user)})


class EntrarPorLinkView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        try:
            share_hash = request.POST.get('share_hash')
            projeto: Projeto = Projeto.objects.get(share_hash=share_hash)

            if projeto.encerrado:
                request.session['error'] = 'Este projeto está encerrado, não pode aceitar mais membros'
                return redirect('projeto-detail', url_hash=projeto.url_hash)

            UsuarioAceito.salvar(projeto, request.user, True)
            return redirect('projeto-detail', url_hash=projeto.url_hash)
        except Projeto.DoesNotExist:
            request.session['error'] = 'Pare de tentar quebrar meu sistema!!!!! >:('
            return redirect('projetos')


class ConvidarView(View):
    @staticmethod
    def post(request, share_hash, *args, **kwargs):
        try:
            projeto: Projeto = Projeto.objects.get(share_hash=share_hash)

            if projeto.encerrado:
                request.session['error'] = 'Este projeto está encerrado, não pode aceitar mais membros'
                return redirect('projeto-detail', url_hash=projeto.url_hash)

            convidados = []
            user_list = request.POST.getlist('convites')

            for item in user_list:
                u: QuerySet[User] = User.objects.filter(Q(email__exact=item) | Q(username__exact=item) |
                                                        Q(profile__url_hash=item))
                if len(u) == 1:
                    _ = u[0]
                    participantes = UsuarioAceito.objects.filter(projeto=projeto, user=_)
                    if len(participantes) == 1:
                        continue

                    UsuarioRecusado.objects.filter(projeto=projeto, user=_).delete()
                    UsuarioBanido.objects.filter(projeto=projeto, user=_).delete()

                    if _ not in convidados:
                        if len(UsuarioConvidado.objects.filter(projeto=projeto, user=_)) < 1:
                            con = UsuarioConvidado(projeto=projeto, user=_)
                            con.save()

                        convidados.append(_)

            request.session['success'] = 'Os usuários digitados receberam o convite, você verá eles na tela ' \
                                         'de participantes caso eles aceitem'

            return redirect('projeto-detail', url_hash=projeto.url_hash)

        except Projeto.DoesNotExist:
            request.session['error'] = 'Como que você fez este POST?'
            return redirect('projetos')


class ConvidarUsuarioView(View):
    @staticmethod
    def post(request, user_hash, *args, **kwargs):
        try:
            user: User = User.objects.get(profile__url_hash=user_hash)
            p: Projeto = Projeto.objects.get(url_hash=request.POST.get('projeto'))

            participantes = UsuarioAceito.objects.filter(projeto=p, user=user)

            if len(participantes) == 1:
                request.session['warning'] = 'Esse usuário já está neste projeto, veja abaixo'
                return redirect('projeto-detail', url_hash=p.url_hash)

            UsuarioRecusado.objects.filter(projeto=p, user=user).delete()
            UsuarioBanido.objects.filter(projeto=p, user=user).delete()

            if len(UsuarioConvidado.objects.filter(projeto=p, user=user)) < 1:
                UsuarioConvidado.salvar(p, user, False)
                request.session['success'] = 'O usuário foi convidado com sucesso'
                return redirect('users')
            else:
                request.session['warning'] = 'Este usuário já foi convidado'
                return redirect('users')

        except User.DoesNotExist:
            request.session['error'] = 'Como você fez este POST? Não quebre meu sistema :('
            return redirect('users')
        except Projeto.DoesNotExist:
            request.session['error'] = 'Como você fez este POST? Não quebre meu sistema :('
            return redirect('users')


class AceitarConviteView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            projeto: Projeto = Projeto.objects.get(share_hash=share_hash)
            user: User = User.objects.get(profile__url_hash=user_hash)

            UsuarioConvidado.salvar(projeto, user, True)
            UsuarioAceito.salvar(projeto, user, True)

            request.session['success'] = 'Parabéns! Você agora está participando de um projeto'
            return redirect('projeto-detail', url_hash=projeto.url_hash)
        except Projeto.DoesNotExist:
            request.session['error'] = 'Por favor, não tente quebrar o sistema :('
            return redirect('projetos')
        except User.DoesNotExist:
            request.session['error'] = 'Por favor, não tente quebrar o sistema :('
            return redirect('projetos')


class RecusarConviteView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            projeto: Projeto = Projeto.objects.get(share_hash=share_hash)
            user: User = User.objects.get(profile__url_hash=user_hash)

            UsuarioConvidado.salvar(projeto, user, True)

            request.session['success'] = 'Você recusou o convite no projeto %s' % projeto.nome
            return redirect('notifications')
        except Projeto.DoesNotExist:
            request.session['error'] = 'Por favor, não tente quebrar o sistema :('
            return redirect('projetos')
        except User.DoesNotExist:
            request.session['error'] = 'Por favor, não tente quebrar o sistema :('
            return redirect('projetos')


class AumentarCargoView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            projeto: Projeto = Projeto.objects.get(share_hash=share_hash)
            user: User = User.objects.get(profile__url_hash=user_hash)

            if projeto.encerrado:
                request.session['error'] = 'Este projeto está encerrado, não é possível realizar alterações'
                return redirect('projeto-detail', url_hash=projeto.url_hash)

            if projeto.moderador == user:
                projeto.moderador = None
                projeto.administrador = user
            else:
                projeto.moderador = user

            projeto.save()

            request.session['success'] = 'Você subiu o cargo do pesquisador %s' % user.first_name
            return redirect('projeto-detail', url_hash=projeto.url_hash)

        except Projeto.DoesNotExist:
            request.session['error'] = 'Por favor, não tente quebrar o sistema :('
            return redirect('projetos')
        except User.DoesNotExist:
            request.session['error'] = 'Por favor, não tente quebrar o sistema :('
            return redirect('projetos')


class RebaixarCargoView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            projeto: Projeto = Projeto.objects.get(share_hash=share_hash)
            user: User = User.objects.get(profile__url_hash=user_hash)

            if projeto.encerrado:
                request.session['error'] = 'Este projeto está encerrado, não é possível realizar alterações'
                return redirect('projeto-detail', url_hash=projeto.url_hash)

            if projeto.administrador == user:
                projeto.moderador = user
                projeto.administrador = None
            else:
                projeto.moderador = None

            projeto.save()

            request.session['success'] = 'Você rebaixou o cargo do pesquisador %s' % user.first_name
            return redirect('projeto-detail', url_hash=projeto.url_hash)

        except Projeto.DoesNotExist:
            request.session['error'] = 'Por favor, não tente quebrar o sistema :('
            return redirect('projetos')
        except User.DoesNotExist:
            request.session['error'] = 'Por favor, não tente quebrar o sistema :('
            return redirect('projetos')


class SolicitarParticipacaoView(View):
    @staticmethod
    def post(request, url_hash, *args, **kwargs):
        try:
            p: Projeto = Projeto.objects.get(url_hash=url_hash)
            p.pendentes.add(request.user)
            p.save()

            request.session['success'] = 'Solicitação enviada'
            return redirect('projeto-detail', url_hash=url_hash)
        except Projeto.DoesNotExist:
            request.session['error'] = 'Por que você fez um post em um projeto que não existe?'
            return redirect('projetos')


class AceitarParticipacaoView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            user: User = User.objects.filter(Q(profile__url_hash=user_hash))[0]
            project: Projeto = Projeto.objects.filter(share_hash=share_hash)[0]

            project.pendentes.remove(user)

            UsuarioAceito.salvar(project, user)

            project.save()

            request.session['success'] = 'O pesquisador %s foi adicionado no projeto %s' % (user.first_name,
                                                                                            project.nome)
            return redirect('notifications')

        except IndexError:
            request.session['error'] = 'Usuário ou projetos inexistentes'


class RecusarParticipacaoView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            user: User = User.objects.filter(Q(profile__url_hash=user_hash))[0]
            project: Projeto = Projeto.objects.filter(share_hash=share_hash)[0]

            project.pendentes.remove(user)

            u = UsuarioRecusado(projeto=project, user=user)
            u.save()

            project.save()

            request.session['success'] = 'O pesquisador %s foi recusado no projeto %s' % (user.first_name,
                                                                                          project.nome)
            return redirect('notifications')

        except IndexError:
            request.session['error'] = 'Usuário ou projetos inexistentes'


class AdvertenciaView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            user: User = User.objects.filter(Q(profile__url_hash=user_hash))[0]
            project: Projeto = Projeto.objects.filter(share_hash=share_hash)[0]

            u = UsuarioAdvertido(projeto=project, user=user)
            u.save()
            user.profile.advertencias += 1
            user.profile.save()

            project.save()

            request.session['success'] = 'O pesquisador %s recebeu uma advertência' % user.first_name
            return redirect('projeto-detail', url_hash=project.url_hash)

        except IndexError:
            request.session['error'] = 'Como você conseguiu realizar este POST?'

        return redirect('projetos')


class GrafificarView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            user: User = User.objects.filter(Q(profile__url_hash=user_hash))[0]
            project: Projeto = Projeto.objects.filter(share_hash=share_hash)[0]

            u = UsuarioGratificado(projeto=project, user=user)
            u.save()
            user.profile.gratificado += 1
            user.profile.save()

            project.save()

            request.session['success'] = 'O pesquisador %s foi gratificado' % user.first_name
            return redirect('projeto-detail', url_hash=project.url_hash)

        except IndexError:
            request.session['error'] = 'Como você conseguiu realizar este POST?'

        return redirect('projetos')


class BanirView(View):
    @staticmethod
    def post(request, share_hash, user_hash, *args, **kwargs):
        try:
            user: User = User.objects.filter(Q(profile__url_hash=user_hash))[0]
            project: Projeto = Projeto.objects.filter(share_hash=share_hash)[0]

            u = UsuarioBanido(projeto=project, user=user)
            u.save()
            user.profile.banido += 1
            user.profile.save()

            k = UsuarioAceito.objects.filter(user=user, projeto=project)
            k.delete()

            project.save()

            request.session['success'] = 'O pesquisador %s foi banido' % user.first_name
            return redirect('projeto-detail', url_hash=project.url_hash)

        except IndexError:
            request.session['error'] = 'Como você conseguiu realizar este POST?'

        return redirect('projetos')


class VisualizarAceitacaoView(View):
    @staticmethod
    def post(request, url_hash, *args, **kwargs):
        try:
            u = UsuarioAceito.objects.get(projeto=Projeto.objects.get(url_hash=url_hash), user=request.user)
            u.visualizou = True
            u.save()
            return redirect('projeto-detail', url_hash=url_hash)
        except Projeto.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'
        except UsuarioAceito.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'

        return redirect('notifications')


class VisualizarRecusacaoView(View):
    @staticmethod
    def post(request, url_hash, *args, **kwargs):
        try:
            u = UsuarioRecusado.objects.get(projeto=Projeto.objects.get(url_hash=url_hash), user=request.user)
            u.visualizou = True
            u.save()
        except Projeto.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'
        except UsuarioAceito.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'

        finally:
            return redirect('notifications')


class VisualizarAdvertenciaView(View):
    @staticmethod
    def post(request, url_hash, *args, **kwargs):
        try:
            u = UsuarioAdvertido.objects.get(projeto=Projeto.objects.get(url_hash=url_hash), user=request.user)
            u.visualizou = True
            u.save()
        except Projeto.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'
        except UsuarioAceito.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'

        finally:
            return redirect('notifications')


class VisualizarGratificacaoView(View):
    @staticmethod
    def post(request, url_hash, *args, **kwargs):
        try:
            u = UsuarioGratificado.objects.get(projeto=Projeto.objects.get(url_hash=url_hash), user=request.user)
            u.visualizou = True
            u.save()
        except Projeto.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'
        except UsuarioAceito.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'

        finally:
            return redirect('notifications')


class VisualizarBanimentoView(View):
    @staticmethod
    def post(request, url_hash, *args, **kwargs):
        try:
            UsuarioBanido.salvar(Projeto.objects.get(url_hash=url_hash), request.user, True)
        except Projeto.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'
        except UsuarioAceito.DoesNotExist:
            request.session['error'] = 'Ocorreu um erro desconhecido, contate o administrador'

        finally:
            return redirect('notifications')


class NotificacaoView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        projetos_aceitar = Projeto.objects.filter(Q(criador=request.user) | Q(administrador=request.user))
        projetos_aceitos = UsuarioAceito.objects.filter(user=request.user, visualizou=False)
        projetos_recusados = UsuarioRecusado.objects.filter(user=request.user, visualizou=False)
        projetos_banidos = UsuarioBanido.objects.filter(user=request.user, visualizou=False)
        projetos_advertidos = UsuarioAdvertido.objects.filter(user=request.user, visualizou=False)
        projetos_gratificados = UsuarioGratificado.objects.filter(user=request.user, visualizou=False)
        projetos_convidados = UsuarioConvidado.objects.filter(user=request.user, visualizou=False)

        qtd_notifications = 0

        for projeto in projetos_aceitar:
            qtd_notifications += len(projeto.pendentes.all())

        qtd_notifications += (len(projetos_aceitos) + len(projetos_recusados) + len(projetos_banidos) +
                              len(projetos_advertidos) + len(projetos_gratificados) + len(projetos_convidados))

        return render(request, 'dashboard/notification/notifications.html',
                      {'current': 'notifications',
                       'qtd_notifications': qtd_notifications,
                       'projetos_aceitar': projetos_aceitar,
                       'projetos_aceitos': projetos_aceitos,
                       'projetos_recusados': projetos_recusados,
                       'projetos_banidos': projetos_banidos,
                       'projetos_advertidos': projetos_advertidos,
                       'projetos_gratificados': projetos_gratificados,
                       'projetos_convidados': projetos_convidados,
                       'success': request.session.pop('success', None),
                       'error': request.session.pop('error', None),
                       'warning': request.session.pop('warning', None),
                       })


class HelpView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'dashboard/help.html', {'current': 'help'})


def ver_qtd_notificacoes(user):
    qtd_notifications = (len(UsuarioAceito.objects.filter(user=user, visualizou=False)) +
                         len(UsuarioRecusado.objects.filter(user=user, visualizou=False)) +
                         len(UsuarioBanido.objects.filter(user=user, visualizou=False)) +
                         len(UsuarioGratificado.objects.filter(user=user, visualizou=False)) +
                         len(UsuarioAdvertido.objects.filter(user=user, visualizou=False)) +
                         len(UsuarioConvidado.objects.filter(user=user, visualizou=False)))

    for projeto in Projeto.objects.filter(Q(criador=user) | Q(administrador=user)):
        qtd_notifications += len(projeto.pendentes.all())

    return qtd_notifications


def add_categorias(lista):
    list_categorias = []

    for item in lista:
        try:
            c = Categoria.objects.filter(nome=item.upper())[0]
        except IndexError:
            c = Categoria(nome=item)
            c.save()

        list_categorias.append(c)

    return list_categorias
