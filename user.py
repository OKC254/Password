class User:
    user_list = []

    def __init__ (self,f_name,m_name,e_mail):

      self.f_name = f_name
      self.m_name = m_name
      self.e_mail = e_mail

    def save_user(self):
        User.user_list.append(self)
    def delete_user(self):
        User.user_list.remove(self)
    @classmethod
    def display_users(cls):
        return cls.user_list
