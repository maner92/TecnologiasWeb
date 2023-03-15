from Logica.Models import usuarios as u


def create_user(nick_name, fullname):
    user = u.Users(nick_name=nick_name, fullname=fullname)
    try:
        u.session.add(user)
        u.session.commit()
        return f"successfull created user {user.nick_name}"
    except Exception as error:
        u.session.rollback()
        raise (error)
